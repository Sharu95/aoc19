for i in {1..24}
  do
    mkdir $i
    touch $i/input.txt
    touch $i/main.py
    echo -e "def main():\n\tpass\n" > $i/main.py
    echo -e "if __name__ == '__main__':" >> $i/main.py
    echo -e "\twith open('input.txt', 'r') as f:\n\t\t_ = f.read()\n\t\tmain()" >> $i/main.py
  done