import mlflow

def add(a, b):
    return a + b

if __name__ == "__main__":
    # Define different sets of parameters
    experiments = [
        {"param_a": 1, "param_b": 2},
        {"param_a": 2, "param_b": 3},
        {"param_a": 3, "param_b": 4}
    ]

    for experiment in experiments:
        # Start MLflow run
        with mlflow.start_run():
            # Log parameters
            mlflow.log_param("param_a", experiment["param_a"])
            mlflow.log_param("param_b", experiment["param_b"])

            # Perform addition
            result = add(experiment["param_a"], experiment["param_b"])

            # Log metrics
            mlflow.log_metric("result", result)

            print(f"Parameters: {experiment}, Result: {result}")