from openpyxl import load_workbook


def savedReply(key):
    print(key)
    #excel library initiated
    wb = load_workbook("convo.xlsx")
    ws = wb.active
    for row in ws.rows:
        if key in row[0].value:
            return row[1].value

    return "Did not understand"

