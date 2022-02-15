world_record = float(input())
distance = float(input())
swim_sec_for_meter = float(input())

sec_he_should_swim = distance * swim_sec_for_meter
resistance = round(distance / 15)
all_resistance = resistance * 12.5
sec_he_swim = sec_he_should_swim + all_resistance

if sec_he_swim < world_record:
    print(f'Yes, he succeeded! The new world record is {sec_he_swim:.2f} seconds.')
else:
    print(f'No, he failed! He was {sec_he_swim - world_record:.2f} seconds slower.')
