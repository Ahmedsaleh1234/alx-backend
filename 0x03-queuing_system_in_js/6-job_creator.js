import { createQueue } from 'kue'

const queue = createQueue({name: 'push_notification_code'});

const jop = queue.create('push_notification_code' , {
    phoneNumber: 'string',
    message: 'string',
})
jop.on('enqueue', () => {
    console.log("Notification job created: ", jop.id)
})
jop.on('complete', () => {
    console.log("Notification job completed")
})
jop.on('failed attemp', () => {
    console.log('Notification job failed')
})
jop.save()