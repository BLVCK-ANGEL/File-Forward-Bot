if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/BLVCK-ANGEL/File-Forward-Bot.git /Forward
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Forward
fi
cd /Forward
pip3 install -U -r requirements.txt
echo "Starting file forward...."
python3 bot.py
