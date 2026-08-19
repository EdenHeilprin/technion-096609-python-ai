# Synthetic transfer case — decision autonomy survey

This teaching example is synthetic. It is not a description of a published study.

Participants complete four statements about decision autonomy at work. They respond to every statement on a scale from 1 (**strongly disagree**) to 7 (**strongly agree**).

Each participant is randomly assigned to one of two item-order conditions, `standard_order` or `reversed_order`. The assignment remains fixed for the entire survey. Items 2 and 4 are reverse-worded.

The export stores one row per participant with an anonymous participant code, the item-order condition, the four raw responses, and a completion flag.

A Python workflow should:

1. verify that the required columns exist;
2. retain completed responses;
3. verify that every retained item response is from 1 through 7;
4. reverse-score items 2 and 4 using `8 - response`;
5. calculate each participant's mean autonomy score;
6. save a participant-level analysis file and a condition-level summary.

The description does not state how a partially completed response should be treated.
