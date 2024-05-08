import kue from 'kue';
/***
 * Task 6. Create the Job creator.
 * Create a queue with Kue
 * Create an object containing the Job data.
 * Create a queue named push_notification_code, and create a job with the object created before
 * When the job is created without error, log to the console Notification job created: JOB ID
 * When the job is completed, log to the console Notification job completed
 * When the job is failing, log to the console Notification job failed
 */
const queue = kue.createQueue();
const job_data = {
	  phoneNumber: '4153518780',
	  message: 'This is the code to verify your account',
};

const name = 'push_notification_code';

const job = queue.create(name, job_data).save((err) => {
	  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
	  console.log('Notification job completed');
});

job.on('failed', () => {
	  console.log('Notification job failed');
});
