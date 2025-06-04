-- 코드를 작성해주세요
select ITEM_ID, ITEM_NAME, RARITY from ITEM_INFO where ITEM_ID in (
select A.ITEM_ID from ITEM_TREE A, ITEM_INFO B where B.RARITY = 'RARE' and B.ITEM_ID = A.PARENT_ITEM_ID
)
order by ITEM_ID desc