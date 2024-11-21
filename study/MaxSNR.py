import numpy as np
import scipy

n_noise_only_frame = np.sum(t < (n_noise_only_frame/sample_rate))
xx_H = np.einsum("mkt,nkt->ktmn",stft_data,np.conjugate(stft_data))
Rn = np.average(xx_H[:,:,:n_noise_only_frame, ...],axis=1)
Rs = np.average(xx_H[:,:,n_noise_only_frame:, ...],axis=1)
max_snr_filter = None

for i k in range(NK):
    w, v = scipy.linalg.eigh(Rs[k, ...], Rn[k, ...])
    if max_snr_filter is None:
        max_snr_filter = v[None, :, -1]
    else:
        max_snr_filter = np.concatenate((max_snr_filter, v[None, :, -1]), axis=0)

Rs_w = np.einsum("kmn, kn->km", np.conjugate(max_snr_filter), Rs_w)
w_max_snr = beta[:, None]*max_snr_filter

c_hat = np.einsum("kmn, kn->km", np.conjugate(w_max_snr), stft_data)

t, maxsnr_out = sp.istft(c_hat, fs=sample_rate, window="hann", nperseg=N)

maxsnr_out = maxsnr_out*iinfo(np.int16).max / 20.0