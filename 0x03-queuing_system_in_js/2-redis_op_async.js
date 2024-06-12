import redis from 'redis';
import { promisify } from 'util';
/***
 * 3. Node Redis client and async operations.
 * Using promisify, modify the function displaySchoolValue
 * to use ES6 async / await.
 */
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('error', (err) => {
	  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
	  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
	  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
	  const value = await getAsync(schoolName);
	  console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
