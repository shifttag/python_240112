import decimal

print(round(1.5))
print("반올림 한 위치 숫자가 짝수 : ", round(2.665, 2))
print("반올림 한 위치 숫자가 짝수 : ", round(2.675, 2))

print("2.675를 정상적으로 반올림 한 결과 : ", decimal.Decimal("2.675").quantize(decimal.Decimal("1.00")))
