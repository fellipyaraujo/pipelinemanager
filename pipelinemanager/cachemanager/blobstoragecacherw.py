import logging
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename='debug.log',level=logging.DEBUG)


def main():
    logging.info('Initialized')


if __name__ == "__main__":
    main()