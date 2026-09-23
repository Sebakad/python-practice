def apply_discount(price, discount):
    """
    Calculate the final price after applying a discount.
    
    Args:
        price (int/float): Original price (must be > 0)
        discount (int/float): Discount percentage (0-100)
    
    Returns:
        float: Final price after discount, or error message
    """
    
    if not isinstance(price, (int, float) ):
        return 'The price should be a number'
    
    elif not isinstance(discount,(int,float)):
        return 'The discount should be a number'
    
    elif price<=0:
        return 'The price should be greater than 0'

    elif discount<0 or discount>100:
        return 'The discount should be between 0 and 100'

    else:
        discount_amount = price*(discount/100)
        return price-discount_amount
    
# Test cases
print(apply_discount(150, 20))      # 80.0
print(apply_discount(50, 5))       # 45.0
print(apply_discount(-100, 10))      # Error message
print(apply_discount(100, 150))     # Error message
print(apply_discount("xyz", 20))    # Error message
