/*
 * Timer_lab4_Busy_Wait
 *
 *  Created on: Apr 8, 2023
 *      Author: Muhammad Alkahwagy
 */

#include "BIT_MATH.h"
#include "STD_TYPES.h"

#include "DIO_Interface.h"
#include "TMR0_Interface.h"

#define LED_PORT    PORTC
#define LED_PIN     PIN0

int main()
{
	TMR0_voidInit();

    DIO_voidSetPinDirection(LED_PORT,LED_PIN,OUTPUT);

    while(1)
    {
        DIO_voidSetPinValue(LED_PORT,LED_PIN,HIGH);

        TMR0_voidSetBusyWaitms(1000);

        DIO_voidSetPinValue(LED_PORT,LED_PIN,LOW);

        TMR0_voidSetBusyWaitms(1000);
    }

    return 0;
}
