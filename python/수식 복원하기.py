def solution(expressions):
    full_string = ''.join(expressions)
    max_digit = 1
    for char in full_string:
        if char.isdigit():
            max_digit = max(max_digit, int(char))  
    bases = set(range(max_digit + 1, 10))
    
    parsed_expressions = [expression.split(' ') for expression in expressions]
    parsed_x_expressions = []
    for parsed_expression in parsed_expressions:
        if parsed_expression[-1] == 'X':
            parsed_x_expressions.append(parsed_expression)
    
    invalid_bases = set()
    for base in bases:
        for A, op, B, eq, C in parsed_expressions:
            if C == 'X':
                continue
            
            a = from_base_to_decimal(A, base)
            b = from_base_to_decimal(B, base)
            c = from_base_to_decimal(C, base)
            if (op == '+' and a + b != c) or (op == '-' and a - b != c):
                invalid_bases.add(base)
                break
    bases -= invalid_bases 
    
    answer = []
    for A, op, B, eq, C in parsed_x_expressions:       
        possible_C = set()
        
        for base in bases:
            a = from_base_to_decimal(A, base)
            b = from_base_to_decimal(B, base)
            if op == '+':
                c = a + b
            elif op == '-':
                c = a - b
            possible_C.add(from_decimal_to_base(c, base))

        C = possible_C.pop() if len(possible_C) == 1 else '?'
                
        answer.append(' '.join([A, op, B, eq, C]))
    
    return answer

def from_base_to_decimal(num_str, base):
    answer = 0
    
    for ch in num_str:
        answer = answer * base + int(ch)
        
    return answer

def from_decimal_to_base(num, base):
    if num == 0:
        return "0"
    
    digits = []
    
    while num > 0:
        digits.append(str(num % base))
        num //= base
        
    return ''.join(reversed(digits))
