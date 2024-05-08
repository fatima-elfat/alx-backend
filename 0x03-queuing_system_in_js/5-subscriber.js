import redis from 'redis';
/***
 * Task 5. Node Redis client publisher and subscriber.
 * create a redis client:
 * On connect, it should log the message Redis client connected to the server
 * On error, it should log the message Redis client not connected to the server: ERROR MESSAGE
 * It should subscribe to the channel holberton school channel
 * When it receives message on the channel holberton school channel, it should log the message to the console
 * When the message is KILL_SERVER, it should unsubscribe and quit
 */
const subscriber = redis.createClient();

subscriber.on('error', (err) => {
	  console.log(`Redis client not connected to the server: ${err.message}`);
});

subscriber.on('connect', () => {
	  console.log('Redis client connected to the server');
});

const ch = 'holberton school channel';
subscriber.subscribe(ch);
subscriber.on('message', (channel, message) => {
	  if (channel === ch) console.log(message);
	  if (message === 'KILL_SERVER') {
		      subscriber.unsubscribe(ch);
		      subscriber.quit();
		    }
});
