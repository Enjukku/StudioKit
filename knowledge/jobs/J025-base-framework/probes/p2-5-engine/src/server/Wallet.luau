--!strict
local Wallet = {}
export type Wallet = { coins: number }
function Wallet.new(): Wallet
	return { coins = 0 }
end
function Wallet.grant(w: Wallet, n: number)
	w.coins += n
end
return Wallet
