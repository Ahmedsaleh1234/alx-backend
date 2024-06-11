import redis from 'redis'

const client = redis.createClient();

client.on('connect', () =>{
    console.log('Redis client connected to the server')
});
client.on('error', (err) => {
    console.error(`edis client not connected to the server:${err}`)
});
client.subscribe('holberton school channel');
client.on('message', (message, channel) => {
    console.log('message  recieved on: ' + channel)
    if (message === 'KILL_SERVER') {
        client.unsubscribe();
        client.quit();
    }
});

