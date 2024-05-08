import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';
/***
 * Task 11. Writing the test for job creation.
 * Import the function createPushNotificationsJobs
 * Create a queue with Kue
 * Write a test suite for the createPushNotificationsJobs function:
 * Use queue.testMode to validate which jobs are inside the queue
etc.
 */
const queue = kue.createQueue();
const expl = [
  {
    phoneNumber: '548965412',
    message: 'This is the code 4796 to verify your account',
  },
  {
    phoneNumber: '748962541',
    message: 'This is the code 7778 to verify your account',
  },
];

describe('createPushNotificationsJobs', () => {
  before(function () {
    queue.testMode.enter();
  });

  afterEach(function () {
    queue.testMode.clear();
  });

  after(function () {
    queue.testMode.exit();
  });

  it('Error 1: Jobs is not an array', () => {
    expect(() => {
      createPushNotificationsJobs(2, queue);
    }).to.throw('Jobs is not an array');
  });

  it('Error 2: Jobs is not an array', () => {
    expect(() => {
      createPushNotificationsJobs('money', queue);
    }).to.throw('Jobs is not an array');
  });

  it('Error 3: Jobs is not an array', () => {
    expect(() => {
      createPushNotificationsJobs({}, queue);
    }).to.throw('Jobs is not an array');
  });

  it('Empty Array', () => {
    const ret = createPushNotificationsJobs([], queue);
    expect(ret).to.equal(undefined);
  });

  it('Test 1: creating queus', () => {
    createPushNotificationsJobs(expl, queue);
    expect(queue.testMode.expl.length).to.equal(2);
    expect(queue.testMode.expl[0].data).to.eql({
      phoneNumber: '548965412',
      message: 'This is the code 4796 to verify your account',
    });
    expect(queue.testMode.expl[1].data).to.eql({
      phoneNumber: '748962541',
      message: 'This is the code 7778 to verify your account',
    });
	expect(queue.testMode.expl[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.expl[1].type).to.equal('push_notification_code_3');
  });
});
