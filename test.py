
import pyupbit

access = "NdCwL4e5r1E3yoS9rgKKxFPTNA6ORT0UZSyFEA02"          # 본인 값으로 변경
secret = "9ENSZLen2yoFjxpzbyCrlCqcOUCCqhLarX3tuMr1"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
