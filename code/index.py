import finetuner
from docarray import DocumentArray

# Login to Jina ecosystem
finetuner.login()

print('Gajraj')
# Prepare training data
# train_data = DocumentArray(...)

# Fine-tune in the cloud
# run = finetuner.fit(
#     model='resnet50', train_data=train_data, epochs=5, batch_size=128,
# )

# print(run.name)
# for log_entry in run.stream_logs():
#     print(log_entry)

# When ready
# run.save_artifact(directory='experiment')