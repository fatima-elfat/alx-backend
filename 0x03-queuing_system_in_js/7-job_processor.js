import kue from 'kue';
/***
 * Task 9. Track progress and errors with Kue: Create the Job processor.
 */
const blacklistedNumber = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
	  job.progress(0, 100);

	  if (blacklistedNumber.includes(phoneNumber)) {
		      done(Error(`Phone number ${phoneNumber} is blacklisted`));
		      return;
		    }

	  job.progress(50, 100);
	  console.log(
		      `Sending notification to ${phoneNumber}, with message: ${message}`
		    );
	  done();
}

const queue = kue.createQueue();
const name = 'push_notification_code_2';
queue.process(name, 2, (job, done) => {
	  const { phoneNumber, message } = job.data;
	  sendNotification(phoneNumber, message, job, done);
});
