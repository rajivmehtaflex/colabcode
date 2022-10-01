import finetuner
finetuner.login()
run = finetuner.fit(
    model='openai/clip-vit-base-patch32',
    run_name='clip-fashion',
    train_data='clip-fashion-train-data',
    eval_data='clip-fashion-eval-data',
    epochs=5,
    learning_rate= 1e-5,
    loss='CLIPLoss',
    cpu=False,
)

print(run.status())

