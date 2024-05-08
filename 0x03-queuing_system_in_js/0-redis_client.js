import redis from 'redis';
/***
 * Task 1. Node Redis Client.
 */
const client = redis.createClient();

client.on('error', (err) => {
	  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
	  console.log('Redis client connected to the server');
});
