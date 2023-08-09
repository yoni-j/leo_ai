import sys

from frequency_service import FrequencyService

if __name__ == '__main__':
    frequency_service = FrequencyService()
    frequency_service.collect_frequency_from_paths(sys.argv[1:])
    frequency_service.print_table()

