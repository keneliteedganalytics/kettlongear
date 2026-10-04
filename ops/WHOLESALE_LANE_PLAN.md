# Wholesale Lane: Plan and Guardrails

Prepared for Kenneth Young, Elite-Edge-Analytics, LLC. 30 September 2026. Since 4 October 2026 this is the only lane: Kettlon Gear is a wholesale-only Amazon store, the private-label budget is folded in (40,000 USD total), and sourcing runs distributor-first under ops/WHOLESALE_SCREEN.md with targets in ops/DISTRIBUTOR_TARGETS.md.

## Bottom line

Yes, a hands-off Amazon resale line is real and we can run it, but not the way it is pitched on Instagram. The version that works is wholesale: buy branded, already-selling products from authorized distributors, ship them straight to a prep center that forwards them into Fulfillment by Amazon (FBA), and let Amazon pick, pack and ship. You never touch a box. What does not work is the "done-for-you Amazon automation store" that pays for itself in 90 days. The Federal Trade Commission (FTC) has shut down several of those operations, including a permanent industry ban for the Click Profit operators in 2025 ([FTC](https://www.ftc.gov/news-events/news/press-releases/2025/08/ftc-case-against-e-commerce-business-opportunity-scheme-its-operators-results-permanent-ban-industry)) and $2.8 million in refunds to DK Automation victims in 2024 ([FTC](https://www.ftc.gov/news-events/news/press-releases/2024/03/ftc-sends-28-million-refunds-consumers-harmed-dk-automations-phony-online-business-crypto)). The scheme is the same each time: sell the dream, buy junk inventory with the client's money, disappear.

Realistic expectation for a disciplined wholesale line: 15 to 30 percent return on inventory capital per turn, 45 to 75 days per turn, first Amazon payout roughly 6 to 8 weeks after the first purchase order. On $12,000 of working inventory that is roughly $1,800 to $3,600 of gross profit per cycle, before software and prep fees. It is a cash-flow engine, not a windfall. We cannot place a purchase order until Amazon clears the identity review on the Kettlon Gear account and until the LLC holds a resale certificate.

## What "never touch the inventory" actually means

1. Distributor ships the case-packed goods to a prep center (third-party warehouse).
2. Prep center inspects, applies the Amazon FNSKU label and any poly bag or bubble wrap, and builds the inbound shipment. Amazon ended its own prep and labeling services on 1 January 2026, so every unit must arrive at Amazon shelf-ready ([AMZ Prep](https://amzprep.com/best-amazon-fba-prep-centers/)). Typical prep runs about $0.75 to $1.50 per unit plus inbound freight.
3. Amazon receives, stores, sells, ships, and handles returns. From 17 April 2026 Amazon adds a 3.5 percent fuel and logistics surcharge to FBA fulfillment fees, and holiday peak fulfillment fees run 15 October 2026 to 14 January 2027 ([Amazon Seller Central](https://sellercentral.amazon.com/help/hub/reference/external/GABBX6GZPA8MSZGW)). Our margin math uses the peak rate card through January.
4. We reorder when the prep center's inventory report and Amazon's restock report say so. All of that is automatable.

## The gates, in order

| Gate | Owner | Why it blocks |
| --- | --- | --- |
| Amazon identity verification clears | Amazon (Ken uploads if asked) | No listings, no inbound shipments until cleared. Amazon says about three business days when documents are clean, longer if they ask for more ([Amazon](https://sell.amazon.com/learn/prepare-to-sell)). |
| Illinois resale certificate (Form CRT-61) and Illinois sales tax registration | Ken, 30 minutes online | Every legitimate distributor requires it to sell to us tax-free. Without it we are buying retail and the margin is gone. |
| Prep center account | Me | Needs the LLC name, EIN, Amazon seller ID. I open the account and set the ship-to address. |
| Distributor accounts (3 to 5) | Me, Ken signs | Applications ask for the resale certificate, EIN, website (kettlongear.com counts), and sometimes a first-order minimum of $500 to $2,000. |
| Ungating | Me | Grocery, Topicals, Beauty and several brands require approval; the approval test is a real distributor invoice for 10 or more units that matches the account exactly ([FBA Tactics](https://fbatactics.com/guides/ungating-restricted-categories/)). We start in open categories and use our first invoices to ungate the rest. |
| ROI screen on 10 or more SKUs | Me, Ken approves the buy list | No purchase order until the SKU passes the screen below. |

## SKU screen (fail any line, no buy)

- Branded product already selling on Amazon with a Best Sellers Rank under 25,000 in its main category and at least 90 days of stable Keepa price history.
- Amazon Retail is not on the listing, or has been out of stock for 60 or more days. We do not fight Amazon for the Buy Box.
- Three to eight FBA sellers on the listing. Fewer means the brand controls distribution and we get shut out; more means a race to the bottom.
- Net margin after referral fee, FBA fee, prep and inbound freight of at least 15 percent of sale price and return on cost of at least 25 percent.
- Distributor is authorized by the brand, confirmed in writing. No liquidators, no "wholesale lists", no Telegram.
- Not seasonal, not hazmat, not meltable (Amazon bans meltables in FBA 15 April to 15 October), not oversize.
- Estimated 30-day sell-through of the whole buy at our price. We would rather buy 24 units of 15 products than 360 units of one.

Everyday, ungated categories that fit this screen: home and kitchen consumables (trash bags, storage, cleaning tools), office and school supplies, pet supplies, tools and hardware, sporting goods accessories, baby products that are not feeding related, and automotive accessories. Grocery, supplements and topicals come later after ungating.

## Budget: $40,000 (original $20,000 plus the $20,000 private-label allocation, folded in 4 October 2026)

| Bucket | Amount | Notes |
| --- | --- | --- |
| Inventory, test lots and first two buys | 28,000 | Test lots of up to $1,000 per distributor (delegated), then Buy 1 of $8,000 and Buy 2 of $12,000 after 21 days of sales data. |
| Prep, labels, inbound freight | 1,800 | Roughly $1.25 per unit for about 1,400 units. |
| Software | 600 | Keepa data ($20 per month) and a repricer ($50 to $100 per month) for six months. Helium 10 is already paid. |
| Ungating invoices and distributor minimums | 1,600 | Small qualifying buys we would sell anyway. |
| Reserve | 8,000 | Returns, removal orders, a bad SKU, Amazon reserve holds. Not touched without Ken. |

Nothing from this budget moves until Ken approves the first buy list line by line. Cards and bank details stay with Ken.

## Automation stack

- Sourcing: Helium 10 Black Box and Xray plus Keepa scans, scored by the ROI screen, output to a weekly buy list in the dashboard.
- Buying: purchase orders drafted from the buy list; Ken approves; I place them in the distributor portals and stop at the payment screen.
- Inbound: prep center receives, labels, ships; I create the Amazon shipment plans.
- Pricing: rule-based repricer holding a floor at our minimum margin, never below cost plus fees.
- Restock: weekly report from Amazon restock tool and prep center stock; reorder triggers when days of cover fall under 30.
- Support: the existing inbox and support automation, plus Amazon buyer messages once live.
- Reporting: every SKU appears in the Kettlon Command dashboard (cost, price, net, ROI, status) with the wholesale budget bar.

## Timeline

| When | What |
| --- | --- |
| Days 0 to 7 | Illinois sales tax registration and CRT-61 (Ken), prep center account, five distributor applications, Keepa subscription, first 200-SKU scan. |
| Days 7 to 21 | Amazon verification clears (expected), distributor approvals, ungating invoices, first buy list of 10 to 15 SKUs to Ken. |
| Days 21 to 35 | Buy 1 placed, goods to prep center, inbound to Amazon, listings live. |
| Days 35 to 60 | First sales, first payout (Amazon pays every 14 days after the first one clears), Buy 2 data. |
| Day 60 onward | Weekly reorder cadence, monthly SKU cull, ungate Grocery and Topicals. |

## What I need from Ken

1. Confirm this $20,000 is separate from the Kettlon product budget.
2. Register for Illinois sales tax and download the CRT-61. I will queue the portal steps to the point where you sign.
3. Approve the first buy list when I send it. That is the only recurring decision on this lane.
