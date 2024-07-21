import modules.async_worker as worker
import time
import args_manager
import csv

def get_task(*args):
  args = list(args)
  args.pop(0)
  return worker.AsyncTask(args=args)

def generate(task: worker.AsyncTask):
  import ldm_patched.modules.model_management as model_management

  with model_management.interrupt_processing_mutex:
    model_management.interrupt_processing = False

  if len(task.args) == 0:
    return

  generation_start = time.perf_counter()
  finished = False
  
  worker.async_tasks.append(task)
  
  while not finished:
    time.sleep(0.1)
    if len(task.yields) > 0:
      flag, product = task.yields.pop(0)
      if flag == 'finish':
        finished = True
  
  generation_time = time.perf_counter() - generation_start
  print(f"Generation time: {generation_time:.2f} seconds")
  return


# read file and generate tasks
print(args_manager.args.imx_prompt_file)

with open(args_manager.args.imx_prompt_file, newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    print(row['prompt'])
    
