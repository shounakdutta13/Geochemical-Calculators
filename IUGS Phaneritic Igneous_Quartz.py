print("IUGS IGNEOUS ROCK CLASSIFICATION FOR PHANETRITIC(PLUTONIC) IGNEOUS ROCKS. ")
print("\n")


def rockName(q_m, a_m, p_m, f_m):
    n_a_m = a_m * (100 / (a_m + p_m))  # n = normalised
    n_p_m = p_m * (100 / (a_m + p_m))

    if f_m == 0:
        if q_m + a_m + p_m == 100:
            if q_m >= 90:
                print("The rock is Quartzolite. ")

            elif 60 < q_m < 90:
                print("The rock is Quartz-rich Granitoid.")

            elif a_m >= 90:
                print("The rock is Alkali Feldspar Syenite.")

            elif p_m >= 90:
                print("The rock may be Diorite, Gabbro or Anorthosite.")

            if 20 < q_m < 60:
                if n_a_m > 90:
                    print("The rock is Alkali Feldspar Granite.")
                elif 10 < n_p_m < 65:
                    print("The given rock is Granite.")
                elif 65 < n_p_m < 90:
                    print("The given rock is Grano-diorite.")
                elif n_p_m > 90:
                    print("The given rock is Tonalite. ")

            if 5 < q_m < 20:
                if n_a_m > 90:
                    print("The given rock is Alkali Feldspar Quartz Syenite.")
                elif 10 < n_p_m < 35:
                    print("The given rock is Quartz Syenite.")
                elif 35 < n_p_m < 65:
                    print("The given rock is Quartz Monzonite.")
                elif 65 < n_p_m < 90:
                    print("The given rock is Quartz Monzodiorte.")
                elif 90 < n_p_m:
                    print("The given rock may be Quartz Diorite or Quartz Gabbro.")

            if q_m < 5:
                if 10 < n_p_m < 35:
                    print("The given rock is Syenite.")
                elif n_a_m > 90:
                    print("The given rock is Alkali Feldspar Syenite.")
                elif n_p_m > 90:
                    print("The given rock maybe Diorite/ Gabbro/ Anorthosite.")
                elif 35 < n_p_m < 65:
                    print("THe given rock is Monzonite.")
                elif 65 < n_p_m < 90:
                    print("The given rock is Monzodiorite.")

        elif q_m + a_m + p_m != 100:                # IF other group of minerals are present like mica group minerals
            nq_q_m = q_m * (100 / (q_m + a_m + p_m))
            nq_a_m = a_m * (100 / (q_m + a_m + p_m))                    # nq = normalised if quartz if present
            nq_p_m = p_m * (100 / (q_m + a_m + p_m))
            nq2_am = nq_a_m * (100 / (nq_a_m + nq_p_m))
            nq2_pm = nq_p_m * (100 / (nq_a_m + nq_p_m))

            if nq_q_m > 90:
                print("The given rock is Quartzolite.")

            elif 60 < nq_q_m < 90:
                print("The rock is Quartz-rich Granitoid.")

            elif 20 < nq_q_m < 60:
                if nq2_am > 90:
                    print("The rock is Alkali Feldspar Granite.")
                elif 10 < nq2_pm < 65:
                    print("The given rock is Granite.")
                elif 65 < nq2_pm < 90:
                    print("The given rock is Grano-diorite.")
                elif nq2_pm > 90:
                    print("The given rock is Tonalite.")

            elif 5 < nq_q_m < 20:
                if nq2_am > 90:
                    print("The given rock is Alkali Feldspar Quartz Syenite.")
                elif 10 < nq2_pm < 35:
                    print("The given rock is Quartz Syenite.")
                elif 35 < nq2_pm < 60:
                    print("The given rock is Quartz Monzonite.")
                elif 60 < nq2_pm < 90:
                    print("The given rock is Quartz Monzodiorite.")
                elif nq2_pm > 90:
                    print("The given rock may be Quartz Diorite or Quartz Gabbro.")

            elif nq_q_m < 5:
                if nq2_am > 90:
                    print("The given rock is Alkali Feldspar Syenite. ")
                elif 10 < nq2_pm < 35:
                    print("The given rock is Syentite.")
                elif 35 < nq2_pm < 65:
                    print("The given rock is Monzonite.")
                elif 65 < nq2_pm < 90:
                    print("The given rock is Monzodiorite.")
                elif nq2_pm > 90:
                    print("The give rock maybe Diorite/ Gabbro/ Anorthosite.")

    elif q_m == 0:
        nf_f_m = f_m * (100 / (f_m + a_m + p_m))  # nf = normailised for feldspathoids
        nf_a_m = a_m * (100 / (f_m + a_m + p_m))
        nf_p_m = p_m * (100 / (f_m + a_m + p_m))
        nf2_am = nf_a_m * (100 / (nf_a_m + nf_p_m))
        nf2_pm = nf_p_m * (100 / (nf_a_m + nf_p_m))
        n_a_m = a_m * (100 / (a_m + p_m))  # n = normalised
        n_p_m = p_m * (100 / (a_m + p_m))

        if f_m + a_m + p_m == 100:
            if f_m > 60:
                print("The given rock is (Foid)olites.")

            elif 10 < f_m < 60:
                if n_a_m > 90:
                    print("The given rock is (Foid)syentie.")
                elif 10 < n_p_m < 50:
                    print("The given rock is (Foid)Monzosyentie.")
                elif 50 < n_p_m < 90:
                    print("The given rock is (Foid)Monzodiorite.")
                elif n_p_m > 90:
                    print("The given rock is (Foid)Gabbro.")

            elif f_m < 10:
                if n_a_m > 90:
                    print("The given rock is (Foid)-bearing ALkali Feldspar Syenite.")
                elif 10 < n_p_m < 35:
                    print("The given rock is (Foid)-bearing Syenite.")
                elif 35 < n_p_m < 65:
                    print("The given rock is (Foid)-bearing Monzonite.")
                elif 65 < n_p_m < 90:
                    print("The given rock is (Foid)- bearing Monzodiorite.")
                elif n_p_m > 90:
                    print("The given rock is (Foid)-bearing Diorite.")

        elif f_m + a_m + p_m != 100:
            if nf_f_m > 60:
                print("The given rock is (Foid)olites.")

            elif 10 < nf_f_m < 60:
                if nf2_am > 90:
                    print("The given rock is (Foid)syentie.")
                elif 10 < nf2_pm < 50:
                    print("The given rock is (Foid)Monzosyentie.")
                elif 50 < nf2_pm < 90:
                    print("The given rock is (Foid)Monzodiorite.")
                elif nf2_pm > 90:
                    print("The given rock is (Foid)Gabbro.")

            elif nf_f_m < 10:
                if nf2_am > 90:
                    print("The given rock is (Foid)-bearing ALkali Feldspar Syenite.")
                elif 10 < nf2_pm < 35:
                    print("The given rock is (Foid)-bearing Syenite.")
                elif 35 < nf2_pm < 65:
                    print("The given rock is (Foid)-bearing Monzonite.")
                elif 65 < nf2_pm < 90:
                    print("The given rock is (Foid)- bearing Monzodiorite.")
                elif nf2_pm > 90:
                    print("The given rock is (Foid)-bearing Diorite.")


q_m = float(input("Enter the modal proportion of Quartz. "))
a_m = float(input("Enter the the modal proportion of Alkali Feldspar. "))
p_m = float(input("Enter the the modal proportion of Plagioclase Feldspar. "))
f_m = float(input("Enter the the modal proportion of Feldspathoid. "))


rockName(q_m, a_m, p_m, f_m,)
