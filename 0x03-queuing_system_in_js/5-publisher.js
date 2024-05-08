import redis from 'redis';
const publisher = redis.createClient();
/***
 * Task 5. Node Redis client publisher and subscriber.
 * On connect, it should log the message Redis client connected to the server
 * On error, it should log the message Redis client not connected to the server: ERROR MESSAGE
 * Write a function named publishMessage
 */
publisher.on('error', (err) => {
	  console.log(`Redis client not connected to the server: ${err.message}`);
});

publisher.on('connect', () => {
	  console.log('Redis client connected to the server');
});

const ch = 'holberton school channel';
function publishMessage(message, time) {
	  setTimeout(() => {
		      console.log(`About to send ${message}`);
		      publisher.publish(ch, message);
		    }, time);
}

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
