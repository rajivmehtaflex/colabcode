import finetuner
finetuner.login()
run = finetuner.get_run('clip-fashion')
print(run.status())
# print(run.logs())