# 1. Load system parameters
# 2. For each SNR:
#      - generate bits using bit_source.py
#      - map bits to QAM symbols
#      - OFDM modulation
#      - pass through channel + noise
#      - OFDM demodulation
#      - equalization
#      - compute BER
# 3. Plot BER vs SNR

