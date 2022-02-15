square_meters = int(input())
total_square_meters = square_meters * 7.61
discount = total_square_meters  * 0.18
final_price = total_square_meters - discount
print('The final price is: %.2f lv.' % final_price)
print('The discount is: %.2f lv.' % discount)