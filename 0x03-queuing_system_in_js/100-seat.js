import kue from 'kue';
import express from 'express';
import { promisify } from 'util';
import redis from 'redis';
/***
 * Redis
 * Kue queue
 * Create a Kue queue
 * Server: express server listening on the port 1245.
 * Requirements:
 * ____Make sure to use promisify with Redis
 * ____Make sure to use the await/async keyword to get the value from Redis
 * ____Make sure the format returned by the web application is always JSON and not text
 * ____Make sure that only the allowed amount of seats can be reserved
 * ____Make sure that the main route is displaying the right number of seats
 */
let resr;
const keys = 'available_seats';
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
function reserveSeat(number) {
  client.set(keys, number);
}
async function getCurrentAvailableSeats() {
  const avlble = await getAsync(keys);
  return avlble;
}
client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});
client.on('connect', () => {
  console.log('Redis client connected to the server');
  reserveSeat(50);
  resr = true;
});
const queue = kue.createQueue();
const name = 'reserve_seat';
const port = 1245;
const app = express();
app.listen(port, () => {
  console.log(`app listening at http://localhost:${port}`);
});

app.get('/available_seats', async (req, res) => {
  const avlble = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: avlble });
});

app.get('/reserve_seat', (req, res) => {
  if (resr === false) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }
  const job = queue.create(name, {}).save((err) => {
    if (err) {
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation in process' });
    }
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

app.get('/process', async (req, res) => {
  queue.process(name, async (job, done) => {
    let avlble = await getCurrentAvailableSeats();

    if (avlble <= 0) {
      done(Error('Not enough seats available'));
    }
    avlble = Number(avlble) - 1;
    reserveSeat(avlble);
    if (avlble <= 0) {
      resr = false;
    }
    done();
  });
  res.json({ status: 'Queue processing' });
});
