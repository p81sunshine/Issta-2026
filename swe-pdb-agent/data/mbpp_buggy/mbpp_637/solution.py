def noprofit_noloss(actual_cost, sale_amount):
  cost = actual_cost if isinstance(actual_cost, float) else float(actual_cost)
  amount = sale_amount if isinstance(sale_amount, float) else float(sale_amount)
  
  if abs(cost - amount) < 1e-10:
    return True
  
  if cost > amount:
    return True
  
  return False