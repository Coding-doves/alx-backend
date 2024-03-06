import kue from 'kue';

// Create a queue with Kue
const queue = kue.createQueue();

// Create an object containing the Job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a test message',
};

// Create a job and add it to the queue
const job = queue.create('push_notification_code', jobData);

// Event listener for successful job creation
job.on('enqueue', (job, type) => {
  console.log(`Notification job created: ${job.id}`);
});

// Event listener for completed job
job.on('complete', () => {
  console.log('Notification job completed');
});

// Event listener for failed job
job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
job.save();
