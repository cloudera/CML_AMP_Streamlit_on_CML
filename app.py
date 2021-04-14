# ###########################################################################
#
#  CLOUDERA APPLIED MACHINE LEARNING PROTOTYPE (AMP)
#  (C) Cloudera, Inc. 2021
#  All rights reserved.
#
#  Applicable Open Source License: Apache 2.0
#
#  NOTE: Cloudera open source products are modular software products
#  made up of hundreds of individual components, each of which was
#  individually copyrighted.  Each Cloudera open source product is a
#  collective work under U.S. Copyright Law. Your license to use the
#  collective work is as provided in your written agreement with
#  Cloudera.  Used apart from the collective work, this file is
#  licensed for your use pursuant to the open source license
#  identified above.
#
#  This code is provided to you pursuant a written agreement with
#  (i) Cloudera, Inc. or (ii) a third-party authorized to distribute
#  this code. If you do not have a written agreement with Cloudera nor
#  with an authorized and properly licensed third party, you do not
#  have any rights to access nor to use this code.
#
#  Absent a written agreement with Cloudera, Inc. (“Cloudera”) to the
#  contrary, A) CLOUDERA PROVIDES THIS CODE TO YOU WITHOUT WARRANTIES OF ANY
#  KIND; (B) CLOUDERA DISCLAIMS ANY AND ALL EXPRESS AND IMPLIED
#  WARRANTIES WITH RESPECT TO THIS CODE, INCLUDING BUT NOT LIMITED TO
#  IMPLIED WARRANTIES OF TITLE, NON-INFRINGEMENT, MERCHANTABILITY AND
#  FITNESS FOR A PARTICULAR PURPOSE; (C) CLOUDERA IS NOT LIABLE TO YOU,
#  AND WILL NOT DEFEND, INDEMNIFY, NOR HOLD YOU HARMLESS FOR ANY CLAIMS
#  ARISING FROM OR RELATED TO THE CODE; AND (D)WITH RESPECT TO YOUR EXERCISE
#  OF ANY RIGHTS GRANTED TO YOU FOR THE CODE, CLOUDERA IS NOT LIABLE FOR ANY
#  DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, PUNITIVE OR
#  CONSEQUENTIAL DAMAGES INCLUDING, BUT NOT LIMITED TO, DAMAGES
#  RELATED TO LOST REVENUE, LOST PROFITS, LOSS OF INCOME, LOSS OF
#  BUSINESS ADVANTAGE OR UNAVAILABILITY, OR LOSS OR CORRUPTION OF
#  DATA.
#
# ###########################################################################

import seaborn as sns
import streamlit as st

st.title("Old Faithful eruptions")

geyser = sns.load_dataset("geyser")

st.markdown(
    """
    This is a tiny app to explore the
    [Old Faithful Geyser Data](https://www.stat.cmu.edu/~larry/all-of-statistics/=data/faithful.dat).
    First, we can view some summary statistics.
    The `duration` variable is the duration of an eruption in minutes,
    and the `waiting` variable is the time between eruptions in minutes.
    """
)

st.write(geyser.describe().T)


"""
So the mean waiting time between eruptions is around 70 minutes,
with a mean eruption duration of three and a half minutes.
Summary statistics can be misleading.
Let us plot the waiting and duration variables against each other.

We'll use a joint density plot, with the marginal densities for each
variable on the corresponding axis.
There are clearly two clusters:
shorter eruptions with a shorter waiting time,
and longer eruptions with a longer waiting time.
These are labeled in our data set, so we separate the data and color by cluster.
"""


with sns.axes_style("white"):
    st.pyplot(
        sns.jointplot(data=geyser, x="waiting", y="duration", hue="kind", kind="kde")
    )