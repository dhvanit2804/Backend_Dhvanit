'''A shopkeeper gives 10% discount on a product. If the product price is 1200, calculate the final price after discount.'''

original_price = 1200
discount_percentage = 10

discount_amount = (discount_percentage / 100) * original_price
final_price = original_price - discount_amount
print(f'Final price after {discount_percentage}% discount is {final_price}')