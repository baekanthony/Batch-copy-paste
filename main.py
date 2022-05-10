import pyperclip
import keyboard
import asyncio

batch = []
results = []

def pasteBatch():
    print("Please paste batch then press Ctrl+D")
    while True:
        line = input()
        if line == "done":
            break
        batch.append(line)

async def iterate():
    for line in batch:
        pyperclip.copy(line)
        print(line)
        # Need to have a small pause here to prevent input from flowing over
        await asyncio.sleep(3)
        print("Ready")
        while True:
            if keyboard.read_key() == "a":
                print("No")
                results.append("No")
                break
            elif keyboard.read_key() == "r":
                print("Yes")
                results.append("Yes")
                break
    print(results)

# Puts output into a nice format for pasting into sheets and copies to clipboard
def getResults():
    result = ""
    for line in results:
        result += (line + "\n")
    pyperclip.copy(result)

async def main():
    pasteBatch()
    await iterate()
    getResults()

if __name__ == '__main__':
    asyncio.run(main())
