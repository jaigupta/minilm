import os

def getLatestCheckpoint(runs_dir: str) -> str:
  if not os.path.isdir(runs_dir):
    return None
  ckpts = os.listdir(runs_dir)
  max_iter = 0
  max_ckpt = None
  for ckpt in ckpts:
    if ckpt.endswith('_checkpoint.tar'):
      try:
        iteration = int(ckpt.split('_')[0])
      except ValueError:
        continue
      if iteration > max_iter:
        max_iter = iteration
        max_ckpt = getCheckpointPath(runs_dir, iteration)
  return max_ckpt


def getCheckpointPath(runs_dir, iteration: int) -> str:
  return os.path.join(runs_dir, f'{iteration}_checkpoint.tar')
