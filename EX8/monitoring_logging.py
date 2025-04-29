import random
import time
import logging
import mlflow

# Step 1: Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Step 2: Define function
def generate_random_data():
    with mlflow.start_run():
        mlflow.log_params({'app_name': 'MyApp', 'version': '1.0'})
        start_time = time.time()

        try:
            while True:
                data = random.randint(1, 100)
                logger.info(f"Generated random data: {data}")
                mlflow.log_metric("my_metric", data)

                uptime = time.time() - start_time
                mlflow.log_metric("app_uptime_seconds", uptime)

                time.sleep(2)

        except KeyboardInterrupt:
            logger.info("Monitoring stopped due to KeyboardInterrupt.")
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
        finally:
            mlflow.end_run()

# Step 3: Main
if __name__ == "__main__":
    logger.info("Monitoring and Logging Application Started.")

    try:
        generate_random_data()
    except Exception as e:
        logger.error(f"Application error: {str(e)}")

    logger.info("Monitoring and Logging Application Stopped.")
