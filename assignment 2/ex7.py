# import relevant modules
import re


# define function
def get_file_metadata(data_as_string: str):
    # initialize some variables needed later
    id = 0
    seq_end_index = 0
    seq_start_index = 0
    data_end_index = 0
    has_date = 0
    has_id = 0
    has_columns = 0
    seq_start = 0
    count = 0

    # 1st for-loop over lines: extract index of Start of Sequence, End of Sequence, and End of Data;
    # and get number of lines of document
    for index, line in enumerate(data_as_string.split('\n')):
        if line == '% SeqHeadStart':
            # extract index of Start of Sequence
            seq_start_index = index
            seq_start = index + 1
        if line == '% SeqHeadEnd':
            # extract index of End of Sequence
            seq_end_index = index
        if line == '% End of data':
            # extract index of End of End
            data_end_index = index
            break
        # get number of lines of Header
        count += 1

    # Check if file format is valid: % SeqHeadEnd or % End of data or % SeqHeadStart are there.
    if not (seq_end_index and seq_start and data_end_index):
        raise AttributeError('% SeqHeadEnd or % End of data or % SeqHeadStart are missing!')

    # Check if % SeqHeadEnd is after SeqHeadStart
    if seq_start_index > seq_end_index:
        raise AttributeError('% SeqHeadEnd is before SeqHeadStart!')

    # get index of line % SeqHeadStart, store it in _excluded, so that it is not in header_lines
    seq_start_index_excluded = seq_start_index + 1
    # get list of indices of header lines
    header_lines = list(range(seq_start_index_excluded, seq_end_index))

    # 2nd for-loop over lines
    for index, line in enumerate(data_as_string.split('\n')):
        # check if there exists a line which is not empty before % SeqHeadStart
        if seq_start_index > index and line != '':
            raise AttributeError('Invalid line before start!')
        # Check if some line of the header is invalid:
        # It only contains lines starting with a % character or empty lines.
        if index in header_lines:
            if not (line == '' or line == '\n' or line.startswith('%')):
                raise AttributeError('Header is not valid.')

            # check if there exists some line which specifies ID, Date and Columns
            if line.startswith('% ID: '):
                has_id = True
            elif line.startswith('% Date'):
                has_date = True
            elif line.startswith('% Columns:'):
                has_columns = True

        # if end of header is reached, check if Date, ID & Column are all there
        if index == count:
            # if not all of ID, Date & Columns exist
            if not (has_id and has_date and has_columns):
                raise AttributeError('Information about Date, ID, or Columns missing!')

        # Get proper ID
        if line.startswith('% ID: '):
            pattern = r'% ID: *(.*)'
            match_id = re.search(pattern, line)
            if match_id:
                id = match_id.group(1)
                # remove leading & trailing whitespaces
                id = id.strip()
                continue
        # Get proper Columns
        elif line.startswith('% Columns: '):
            pattern = r'% Columns: *(.*)'
            match_column = re.search(pattern, line)
            if match_column:
                column_string = match_column.group(1)
                columns = column_string.split(';')
                continue
        # get proper Date
        elif line.startswith('% Date: '):
            pattern = r'% Date: *(.*)'
            match_date = re.search(pattern, line)
            if match_date:
                date_string = match_date.group(1)
                # Check if date is a string
                try:
                    date = int(date_string)
                except:
                    raise TypeError('Cannot convert date to integer!')
                continue

    # return ID as string
    # Data entry as int
    # Column names as list of strings
    return id, date, columns
