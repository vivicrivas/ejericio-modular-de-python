# logica de calculo y filtrado
def get_total_stock(stock_list: list) -> int:
    """"Calcula el stock total sumando las cantidades en la lista de stock."""
    total = 0
    for quantity in stock_list:
        total = total + quantity  # se abrevia como total += quantity
        return total


def get_low_stock_count(stock_list: list, limit: int) -> int:
    """"cuenta cuántos productos tienen un stock por debajo del límite dado."""
    count = 0
    index = 0

    while index < len(stock_list):
        if stock_list[index] < limit:
            count += 1
        index += 1  # se suma + 1 al index para moverse al siguiente elemento de la lista
    return count
