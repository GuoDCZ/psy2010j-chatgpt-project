import openai
import argparse
import os
import time

def cmpl_request(prompt):
    messages = [{'role':'user','content':prompt}]
    cmpl = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo", 
        messages = messages, 
        temperature = 1.0,
        presence_penalty = .0, 
        frequency_penalty = .0
    )
    response = cmpl["choices"][0]["message"]['content']
    return response

def parse_command_line():
    parser = argparse.ArgumentParser(description="A simple chatBot using Openai gpt-3.5-turdo model")
    parser.add_argument('file', type=str, nargs=1,
                        help='Specify a file as a prompt collections.')
    return parser.parse_args()

def task(fileName, repetition):
    f = open(fileName)
    line = f.readline()
    q = 0
    while line:
        print(f'[Q{q+1}]')
        print(line.strip('\n'))
        for a in range(0, repetition):
            try:
                response = cmpl_request(line)
                print(f'[A{a+1}]')
                print(response)
            except:
                time.sleep(1)
                a -= 1
        line = f.readline()
        print()
        q+=1
    f.close()

def main():
    args = parse_command_line()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    task(args.file[0], 50)

if __name__ == '__main__':
    main()
