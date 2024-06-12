import { createQueue } from "kue";

const queue = createQueue()

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
}
queue.process('push_notification_code' ,(jop, done) => {
    sendNotification(jop.data.phoneNumber, jop.data.message)
    done();
})