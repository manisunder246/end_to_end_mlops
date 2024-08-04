def add(a, b):
    return a + b

if __name__ == "__main__":
    # Start MLflow run
    with mlflow.start_run():
        # Log parameters
        mlflow.log_param("param_a", 1)
        mlflow.log_param("param_b", 2)

        # Perform addition
        result = add(1, 2)

        # Log metrics
        mlflow.log_metric("result", result)

        print(f"Result: {result}")