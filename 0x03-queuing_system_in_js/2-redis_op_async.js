import redis, { createClient } from 'redis'
import { promisify } from 'util'

const client = createClient()

client.on('connect', () =>{
    console.log('Redis client connected to the server')
})
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`)
})
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print)
}
async function displaySchoolValue(schoolName) {
    const getkey = promisify(client.get).bind(client)
    const value = await getkey(schoolName)
    console.log(value)
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');