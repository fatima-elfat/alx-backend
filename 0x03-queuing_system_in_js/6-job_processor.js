import kue from 'kue';
/***
 * Task 7. Create the Job processor.
 * Create a queue with Kue
 * Create a function named sendNotification
 * Write the queue process that will listen to new jobs on push_notification_code
 */
const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
	  console.log(
		      `Sending notification to ${phoneNumber}, with message: ${message}`
		    );
}

const name = 'push_notification_code';

queue.process(name, (job, done) => {
	  const { phoneNumber, message } = job.data;
	  sendNotification(phoneNumber, message);
	  done();
});
