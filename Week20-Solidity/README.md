# Corporate finance smart contracts in Solidity

## Summary

In this activity we create three smart contracts to help with a hypothetical company's finances.

The [AssociateProfitSplitter](./AssociateProfitSplitter.sol) contract allows an HR department to pay employees quickly. The payroll manager can send ETH to the contract, which will divide it equally among the associates.

The [TieredProfitSplitter](./TieredProfitSplitter.sol) contract is similar to the previous one except that it is initialized with different percentages associated with each employee (e.g., 60% for CEO, 25% for CFO, etc.).

The [DeferredEquityPlan](./DeferredEquityPlan.sol) contract controls the distribution of equity among associates. An associate can call the contract to claim any shares that have vested.

## Deployed contracts

The three contracts have been deployed on the Kovan Testnet Network:

* AssociateProfitSplitter: https://kovan.etherscan.io/address/0xb56d734040fb24a0c4ef9f664eb31a655aec6c5e

* TieredProfitSplitter: https://kovan.etherscan.io/address/0x29abbfe7f74a22c62db1c287378aeb8baeb7f084

* DeferredEquityPlan: https://kovan.etherscan.io/address/0xdc9fa8b8b5d0ff3e67e2bc8c1c6a24b2e7b54c4b

## Interacting with contracts

[Remix](https://remix.ethereum.org) can be used to call the contracts. To do so, import the `.sol` file or copy the content therein to an empty file in Remix. After compiling the code, select the Deployment tab. Toward the bottom of the tab there's a field titled "At Address". Enter the address of the contract you wish to use and click the "At Address" button. The contract will appear under "Deployed Contracts" below the address field.

Please note that these contracts have specific rules that constrain who can call certain actions on the contract. For example, anyone can view the balance of distributed shares in `DeferredEquityPlan`, but only HR and the employee can distribute shares. If you're viewing the contract linked above, therefore, functionality will be restricted.
