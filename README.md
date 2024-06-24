# Catastrophic-risk-aware reinforcement learning with extreme-value-theory-based policy gradients

Abstract

This paper tackles the problem of mitigating catastrophic risk (which is risk with very
low frequency but very high severity) in the context of a sequential decision making process.
This problem is particularly challenging due to the scarcity of observations in the far tail
of the distribution of cumulative costs (negative rewards). A policy gradient algorithm is
developed, that we call POTPG. It is based on approximations of the tail risk derived from
extreme value theory. Numerical experiments highlight the out-performance of our method
over common benchmarks, relying on the empirical distribution. An application to financial
risk management, more precisely to the dynamic hedging of a financial option, is presented
