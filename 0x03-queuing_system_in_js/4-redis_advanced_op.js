#!/usr/bin/yarn dev
import redis from 'redis';

const client = redis.createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const createHash = () => {
	client.hset('HolbertonSchools', 'Portland', 50, redis.print);
	client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
	client.hset('HolbertonSchools', 'New York', 20, redis.print);
	client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
	client.hset('HolbertonSchools', 'Cali', 40, redis.print);
	client.hset('HolbertonSchools', 'Paris', 2, redis.print);
}

const printHash = (hashName) => {
  client.HGETALL(hashName, (_err, reply) => console.log(reply));
};

createHash();
printHash('HolbertonSchools');
