# Wholesale Sourcing Screen, Version 2

Effective 4 October 2026. Replaces the product-first screen in ops/WHOLESALE_SHORTLIST.md (30 September 2026). Kettlon Gear is now a wholesale-only Amazon store. No private-label product development, samples, tooling or brand listings.

## Bottom line

The September screen started from Helium 10 Black Box product rows and then looked for a supplier. That produced 200 rows, 27 survivors and 5 quote requests, and 1 of the 5 declined because the brand owner sells on Amazon itself. Almost every survivor was a private-label brand whose only seller is the brand, which is exactly the product a wholesaler cannot buy. The new screen runs the other way: open distributor accounts first, pull their price lists, then check each item against Amazon. Price list in, Keepa out.

## Stage 1: distributor gate (before any product work)

A distributor goes on the active list only if all four hold.

1. Authorized by the brands it carries (manufacturer-direct or named on the brand's distributor page). No liquidators, no closeout lots, no "Amazon supplier lists", no Telegram or WhatsApp sellers, no sites that advertise "FBA ungating invoices" as a service.
2. Sells to businesses without a brick-and-mortar store, or has not stated a storefront requirement. Disclosed Amazon resale is not a stated reason for refusal.
3. Opening order at or under 1,000 USD so a first order fits the delegated authority in ops/AUTHORITY.md.
4. Ships to a third-party prep center address.

Target list and status: ops/DISTRIBUTOR_TARGETS.md.

## Stage 2: price-list screen (fail any line, drop the item)

Run on every line of a distributor price list once the account is open. Tools: Helium 10 Xray or Black Box ASIN lookup, Keepa 90-day chart, Amazon Revenue Calculator.

| Test | Pass condition | Why |
|---|---|---|
| Listing exists | A live Amazon ASIN for the exact item and pack size, matched by UPC | We join existing listings, we do not build them |
| Brand is not the seller | Brand name differs from the seller names on the offer list, and the brand has no "Visit the Store" Amazon-only strategy that excludes resellers | Brand-direct listings shut resellers out |
| Seller count | 3 to 8 FBA offers, excluding Amazon Retail | Under 3 means controlled distribution, over 8 means a price race |
| Amazon Retail | Not on the listing, or out of stock 60 of the last 90 days on Keepa | We do not fight Amazon for the Buy Box |
| Rank | Best Sellers Rank under 25,000 in a top-level open category, stable on Keepa for 90 days | Demand that is real and not a spike |
| Category | Home and Kitchen, Tools and Home Improvement, Pet Supplies, Automotive, Sports and Outdoors, Office Products, Toys and Games, Patio Lawn and Garden, Musical Instruments, Arts Crafts and Sewing, Industrial and Scientific. Grocery, Topicals, Beauty, Health and Household and Baby feeding items wait until the account is ungated with real invoices | Open categories first |
| Weight and size | Under 2 lb shipped, standard size tier, not oversize | FBA fees on heavy goods eat the margin |
| Price band | 15 to 50 USD sale price | Under 15 the fees take the margin, over 50 the capital turns too slowly |
| Returns | No Frequently Returned Item badge, return rate under 5 percent where visible | Returns are a cost line |
| Hazmat and meltables | None. No aerosols, lithium cells, liquids over 100 ml, chocolate or wax | Prep center and FBA restrictions |
| Seasonality | No single-season items in the first two buys | Capital must turn |
| Margin | Net margin at least 20 percent of sale price after referral fee, FBA fulfillment fee at the peak rate card through 14 January 2027, prep at 1.25 USD per unit and inbound freight. Return on cost at least 30 percent | Floor that survives a price drop |
| Sell-through | The planned buy sells in 30 days at our share of the Buy Box (estimated monthly units divided by seller count plus one) | We buy 24 units of 15 items, not 360 of one |

Max buy cost formula, per unit: (sale price x 0.85) minus FBA fulfillment fee minus 1.25 prep and freight, divided by 1.30. Verify in the Amazon Revenue Calculator before any order.

## Stage 3: order rules

- First order per distributor is a test lot: 10 to 15 SKUs, 12 to 24 units each, total at or under 1,000 USD. Delegated authority covers it. Anything above 1,000 USD waits for Ken.
- Every first-order invoice is kept as the ungating invoice for the brand and category.
- Reorder when Amazon days of cover fall under 30 and the 30-day sell-through held.
- Cull any SKU that misses 60 percent of its 30-day sell-through estimate or whose Buy Box price falls under our floor for 14 days.

## What the September scan can still do

The 200 Black Box rows remain in data/wholesale_scan_raw.json for category demand reference only. The Toyota 90915-YZZD3 filter, Wahl Pocket Pro, Repashy and AFP sun shield requests stay open because each has a real distributor behind it. No other row from that scan is actionable under this screen.
