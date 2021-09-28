import requests
import argparse
import urllib.parse
import shutil

from .questions import questions
from .path import get_path_from_root

parser = argparse.ArgumentParser(description='Make a static copy of the data from the API')
parser.add_argument(
  '--server',
  default='http://localhost:8000',
  help='URL of the server hosting the API',
)
args = parser.parse_args()

out_folder = get_path_from_root('static')
shutil.rmtree(str(out_folder), ignore_errors=True)
out_folder.mkdir()

def get_url(relative_path):
  return urllib.parse.urljoin(args.server, relative_path)

r = requests.get(get_url('/questions'))
r.raise_for_status()
(out_folder / 'questions').write_bytes(r.content)
