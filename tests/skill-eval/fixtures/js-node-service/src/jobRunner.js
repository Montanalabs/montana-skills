export async function runJob(job, logger = console) {
  try {
    await job();
    logger.info("job completed");
  } catch {
    logger.info("job failed");
  }
}
