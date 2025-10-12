import os

BASE_DIR='/content/drive/MyDrive'
DATASETS_DIR=os.path.join(BASE_DIR, 'datasets')
RUNS_DIR=os.path.join(BASE_DIR, 'runs')

def dataset_dir(corpus_name: str) -> str:
  return os.path.join(DATASETS_DIR, corpus_name)

def runs_dir(run_name: str) -> str:
  return os.path.join(RUNS_DIR, run_name)
